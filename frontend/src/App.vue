<template>
  <MovieDetails />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MovieDetails from '@/components/MovieDetails.vue';

export default defineComponent({
  name: 'App',
  components: {
    MovieDetails,
  },
});
</script>