# Shared API Routes

This directory holds shared API route constants for Carbon Sense clients.

## Route prefix

All backend routes are prefixed with `/api`.

## Shared constants

Use `api/routes.ts` from any TypeScript client (extension/web) to avoid route drift:

- `CARBONSENSE_API_PREFIX`
- `CARBONSENSE_API_ROUTES.optimize`
- `CARBONSENSE_API_ROUTES.cacheCheck`
- `CARBONSENSE_API_ROUTES.cacheStore`
- `CARBONSENSE_API_ROUTES.metrics`
- `CARBONSENSE_API_ROUTES.reset`
- `CARBONSENSE_API_ROUTES.health`

## Backend examples

- `POST /api/optimize`
- `POST /api/cache/check`
- `POST /api/cache/store`
- `GET /api/metrics`
- `POST /api/demo/reset`
- `GET /api/health`

## Run backend (port 8080)

```bash
cd api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8080
```

Or run everything (venv + install + seed + server):

```bash
cd api
bash start.sh
```

## Verify

```bash
curl http://localhost:8080/api/health
```