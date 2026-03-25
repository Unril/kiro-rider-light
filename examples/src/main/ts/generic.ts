/** Generic syntax showcase for TypeScript token scopes. */

type TsId = number;
type TsResult<T> = { ok: true; value: T } | { ok: false; error: string };

const TS_MAX_RETRIES = 3 as const;

enum TsRole {
  Admin = "ADMIN",
}

interface TsRepository<T> {
  findById(id: TsId): T | undefined;
}

interface TsUser {
  readonly id: TsId;
  name: string;
  roles: Set<TsRole>;
}

class TsUserRepository implements TsRepository<TsUser> {
  private readonly store = new Map<TsId, TsUser>();

  constructor(private readonly label: string) {}

  findById(id: TsId): TsUser | undefined {
    return this.store.get(id);
  }

  save(user: TsUser): TsResult<TsUser> {
    this.store.set(user.id, user);
    return { ok: true, value: user };
  }
}

const isAdmin = (user: TsUser): boolean => user.roles.has(TsRole.Admin);

async function tsFetch<T>(repo: TsRepository<T>, id: TsId): Promise<TsResult<T>> {
  const item = repo.findById(id);
  if (item === undefined) {
    return { ok: false, error: `not found: ${id}` };
  }
  return { ok: true, value: item };
}

async function tsRetry<T>(block: () => Promise<T>): Promise<T> {
  let last: unknown;
  for (let i = 0; i < TS_MAX_RETRIES; i++) {
    try {
      return await block();
    } catch (e: unknown) {
      last = e;
    }
  }
  throw last instanceof Error ? last : new Error(String(last));
}

// showcase: destructuring, optional chaining, ??, satisfies, as const, typeof
function tsShowcase(obj: unknown, repo: TsUserRepository): string {
  const user = obj instanceof Object && "id" in obj ? (obj as TsUser) : undefined;
  const name = user?.name ?? "anonymous";
  const hex = 0xff;
  const fp = 3.14;
  const ch = "T";
  const config = { retries: TS_MAX_RETRIES } satisfies Record<string, number>;
  const kind = typeof obj === "string" ? "string" : "other";
  return `${name} ${hex} ${fp} ${ch} ${config.retries} ${kind}`;
}

export type { TsId, TsResult, TsUser };
export { TsRole, TsUserRepository, isAdmin, tsFetch, tsRetry, tsShowcase };
