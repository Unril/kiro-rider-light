/** Generic syntax showcase for JavaScript token scopes. */

const JS_MAX_RETRIES = 3;

const JsRole = Object.freeze({
  Admin: "ADMIN",
});

class JsUserRepository {
  #store = new Map();

  findById(id) {
    return this.#store.get(id);
  }

  save(entity) {
    this.#store.set(entity.id, entity);
    return entity;
  }

  findAll() {
    return Array.from(this.#store.values());
  }
}

const jsDisplayName = ({ name, id }) => `${name} (id=${id})`;

async function jsRetry(block, maxAttempts = JS_MAX_RETRIES) {
  let last;
  for (let i = 0; i < maxAttempts; i++) {
    try {
      return await block();
    } catch (e) {
      last = e instanceof Error ? e : new Error(String(e));
    }
  }
  throw last ?? new Error(`failed after ${maxAttempts} attempts`);
}

/** Showcase: object literal, spread, optional chaining, array methods. */
function jsShowcase(obj, repo) {
  const user = repo.findById(1);
  const name = user?.name ?? "anonymous";
  const copy = { ...obj, label: name };
  const admins = repo.findAll().filter((u) => u.roles?.has(JsRole.Admin));
  const hex = 0xff;
  const fp = 3.14;
  const ch = "J";
  return `${name} ${hex} ${fp} ${ch} ${admins.length} ${copy.label}`;
}

module.exports = { JsRole, JsUserRepository, jsDisplayName, jsRetry, jsShowcase };
