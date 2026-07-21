import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchAllCourses = createAsyncThunk('courses/fetchAll', async () => {
  return [
    { id: 1, title: 'Python Programming' },
    { id: 2, title: 'Machine Learning' },
    { id: 3, title: 'Java Development' },
    { id: 4, title: 'Internet of Things (IoT)' },
    { id: 5, title: 'UI/UX Design' }
  ];
});

const courseSlice = createSlice({
  name: 'courses',
  initialState: { items: [], loading: false, error: null },
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload; // This will now be your list above
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      });
  },
});

export const selectCourses = (state) => state.courses.items;
export const selectCoursesLoading = (state) => state.courses.loading;

export default courseSlice.reducer;