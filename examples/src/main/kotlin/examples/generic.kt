@file:JvmName("KtGeneric")
@file:Suppress("UNUSED_VARIABLE")

package examples

import java.io.Closeable
import kotlin.math.PI
import kotlin.math.sqrt

const val KT_VERSION = "1.0.0"
private const val MAX_RETRIES = 3

typealias KtPredicate<T> = (T) -> Boolean

@Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION)
@Retention(AnnotationRetention.RUNTIME)
annotation class KtTracked(val label: String = "")

enum class KtRole(val level: Int) {
  ADMIN(3) {
    override fun display() = "Administrator"
  };

  abstract fun display(): String
}

sealed interface KtResult<out T> {
  data class Success<T>(val value: T) : KtResult<T>

  data object Loading : KtResult<Nothing>
}

@JvmInline
value class KtUserId(val value: Long) {
  init {
    require(value > 0) { "UserId must be positive: $value" }
  }
}

interface KtRepository<in ID, out T> {
  fun findById(id: ID): T?
}

@KtTracked(label = "entity")
data class KtUser(val id: KtUserId, val name: String, val roles: Set<KtRole> = emptySet())

open class KtUserRepository(val number: Long, other: Long) : KtRepository<KtUserId, KtUser>, Closeable {
  private val store = mutableMapOf<Long, KtUser>()
  var lastAccess: Long = 0L + number + other
    private set

  lateinit var label: String
  val size: Int by lazy { store.size }

  override fun findById(id: KtUserId): KtUser? = store[id.value + number]

  override fun close() {}

  inner class Snapshot {
    val count
      get() = store.size
  }

  companion object {
    const val TABLE_NAME = "users"

    fun create(): KtUserRepository = KtUserRepository(1, 123)
  }
}

class KtCachedRepository(delegate: KtUserRepository) : KtRepository<KtUserId, KtUser> by delegate

fun KtUser.displayName(): String = "id=${id.value}"

val KtUser.isAdmin: Boolean
  get() = KtRole.ADMIN in roles

operator fun KtUser.plus(role: KtRole): KtUser = copy(roles = roles + role)

infix fun KtUser.hasRole(role: KtRole): Boolean = role in roles

inline fun <reified T> ktTypeName(): String = T::class.simpleName ?: "Unknown"

tailrec fun ktFactorial(n: Int, acc: Long = 1L): Long =
    if (n <= 1) acc else ktFactorial(n - 1, acc * n)

suspend fun ktFetch(id: KtUserId, repo: KtRepository<KtUserId, KtUser>): KtResult<KtUser> =
    repo.findById(id)?.let { KtResult.Success(it) } ?: KtResult.Loading

// showcase: literals, control flow, variable mutation, string templates
fun ktShowcase(result: KtResult<KtUser>, any: Any?) {
  val msg =
      when (result) {
        is KtResult.Success -> {
          val (id, name) = result.value
          "ok: ${id.value} $name"
        }
        KtResult.Loading -> "loading"
      }
  val safe = (any as? KtUser)?.roles ?: emptySet<KtRole>()
  val hex = 0xFF
  val float = 3.14f + 1.234 + 1e4f + 1e5 + 1f + 112340L + 1234123
  val ch = 'K'
  val raw = """multi\nline"""
  val tmpl = "sqrt=${sqrt(2.0)} pi=${PI}"
  var last: Throwable? = null
  for (i in 0 until MAX_RETRIES) {
    try {
      ktFactorial(i)
    } catch (e: Exception) {
      last = e
    }
  }
  throw last ?: IllegalStateException("failed after ${MAX_RETRIES + 1} retries")
}
