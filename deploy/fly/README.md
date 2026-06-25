# Fly deployment

This fork deploys Bifrost to Fly.io from GitHub Actions.

The Fly image extends the upstream published `maximhq/bifrost:latest` image and
injects this deployment's Postgres-backed config. This keeps production deploys
on published Bifrost releases instead of depending on the upstream `dev` branch
building cleanly at every commit.

## Production resources

- Fly app: `bifrost-gateway-eyhn-nrt`
- Region: `nrt`
- Postgres: Fly Managed Postgres
- Bifrost storage:
  - `config_store`: Postgres
  - `logs_store`: Postgres

## Runtime secrets

The Fly app requires these secrets:

- `BIFROST_ENCRYPTION_KEY`
- `DATABASE_URL`

These are set on the Fly app, not in GitHub. GitHub only needs:

- `FLY_API_TOKEN`

`DATABASE_URL` is created by `fly mpg attach`. The container entrypoint parses it
into the `PG_*` variables that Bifrost's config store expects.

## Deploy

Push to `dev` or run the `Deploy to Fly` workflow manually.

```bash
fly deploy
```

## Update from upstream

```bash
git fetch upstream
git checkout dev
git merge upstream/dev
git push origin dev
```
