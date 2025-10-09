import { configureStore } from '@reduxjs/toolkit';
// Import slices here, e.g., import authSlice from './slices/authSlice';

export const store = configureStore({
  reducer: {
    // Add reducers here, e.g., auth: authSlice,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;