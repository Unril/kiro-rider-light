package examples;

import java.util.*;
import java.util.Optional;

/** Generic syntax showcase for Java token scopes. */
@SuppressWarnings("unused")
class Generic {

  static final int MAX_RETRIES = 3;

  enum JvRole {
    ADMIN
  }

  interface JvRepository<T, ID> {
    Optional<T> findById(ID id);
  }

  record JvUser(long id, String name, Set<JvRole> roles) {
    JvUser(long id, String name) {
      this(id, name, Set.of());
    }

    String displayName() {
      return "%s (id=%d)".formatted(name, id);
    }
  }

  sealed interface JvResult<T> permits JvResult.Ok {
    record Ok<T>(T value) implements JvResult<T> {}
  }

  static class JvUserRepository implements JvRepository<JvUser, Long> {
    private final Map<Long, JvUser> store = new HashMap<>();

    @Override
    public Optional<JvUser> findById(Long id) {
      return Optional.ofNullable(store.get(id));
    }

    JvResult<JvUser> save(JvUser user) {
      store.put(user.id(), user);
      return new JvResult.Ok<>(user);
    }
  }

  @FunctionalInterface
  interface JvSupplier<T> {
    T get() throws Exception;
  }

  static <T> T jvRetry(JvSupplier<T> block) throws Exception {
    Exception last = null;
    for (int i = 0; i < MAX_RETRIES; i++) {
      try {
        return block.get();
      } catch (Exception e) {
        last = e;
      }
    }
    throw Objects.requireNonNullElse(last, new IllegalStateException("failed after " + MAX_RETRIES));
  }

  // switch expr, text block, instanceof pattern, streams, var, literals
  static String jvShowcase(Object obj, List<JvUser> users) {
    String kind = switch (obj) {
      case JvUser u when u.roles().contains(JvRole.ADMIN) -> "admin:" + u.name();
      case JvUser u -> "user:" + u.name();
      case Integer i -> "int:" + i;
      case null -> "null";
      default -> "other";
    };
    String json = """
        {"kind": "%s"}
        """.formatted(kind);
    boolean isAdmin = obj instanceof JvUser u && u.roles().contains(JvRole.ADMIN);
    var names = users.stream().map(JvUser::name).toList();
    int hex = 0xFF;
    double fp = 3.14f + 1.234 + 1e4f + 1e5 + 1f + 112340L + 1234123;
    char ch = 'J';
    return json;
  }
}
