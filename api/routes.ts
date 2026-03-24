export const CARBONSENSE_API_PREFIX = '/api';

export const CARBONSENSE_API_ROUTES = {
  optimize: `${CARBONSENSE_API_PREFIX}/optimize`,
  cacheCheck: `${CARBONSENSE_API_PREFIX}/cache/check`,
  cacheStore: `${CARBONSENSE_API_PREFIX}/cache/store`,
  metrics: `${CARBONSENSE_API_PREFIX}/metrics`,
  reset: `${CARBONSENSE_API_PREFIX}/demo/reset`,
  health: `${CARBONSENSE_API_PREFIX}/health`,
} as const;

export type CarbonSenseApiRouteKey = keyof typeof CARBONSENSE_API_ROUTES;
