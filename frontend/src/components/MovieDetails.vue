<template>
  <div class="min-h-screen bg-[#0D253F]">
    <!-- Header -->
    <header class="bg-[#0D253F] text-white">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center gap-4 md:gap-8">
          <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" alt="TMDB Logo" class="h-5 md:h-8">

          <nav class="hidden md:flex gap-4 lg:gap-8 text-white">
            <a href="#" class="hover:text-[#01B4E4]">Movies</a>
            <a href="#" class="hover:text-[#01B4E4]">TV Shows</a>
            <a href="#" class="hover:text-[#01B4E4]">People</a>
            <a href="#" class="hover:text-[#01B4E4]">More</a>
          </nav>
        </div>

        <div class="flex items-center gap-2 md:gap-6">
          <button class="md:hidden text-white hover:text-[#01B4E4]">
            <Menu class="w-6 h-6" />
          </button>
          <button class="hidden md:block text-white hover:text-[#01B4E4]">
            <Plus class="w-5 h-5" />
          </button>
          <button class="hidden md:block border border-white px-2 py-1 rounded hover:border-[#01B4E4] hover:text-[#01B4E4]">
            EN
          </button>
          <button class="hidden md:block hover:text-[#01B4E4]">Login</button>
          <button class="hidden md:block hover:text-[#01B4E4]">Join TMDB</button>
          <button class="text-[#01B4E4]">
            <Search class="w-5 h-5" />
          </button>
        </div>
      </div>
    </header>

    <!-- Secondary Navigation -->
    <nav class="bg-white border-b border-gray-200">
      <div class="container mx-auto px-4">
        <div class="flex justify-center gap-8">
          <button class="py-3 px-2 border-b-4 border-[#01B4E4] font-semibold">Overview</button>
          <button class="py-3 px-2 text-gray-600 hover:text-gray-900">Media</button>
          <button class="py-3 px-2 text-gray-600 hover:text-gray-900">Fandom</button>
          <button class="py-3 px-2 text-gray-600 hover:text-gray-900">Share</button>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main v-if="movie" class="relative">
      <!-- Background Image with Overlay -->
      <div class="absolute inset-0 bg-[url('https://image.tmdb.org/t/p/w1920_and_h800_multi_faces/aos4s0qTozNb9RQrsIR3m85z70d.jpg')] bg-cover bg-center">
        <div class="absolute inset-0 bg-[#0D253F]/90"></div>
      </div>

      <!-- Content -->
      <div class="relative container mx-auto px-4 py-8">
        <div class="flex flex-col lg:flex-row gap-8">
          <!-- Poster -->
          <div class="lg:w-1/3 xl:w-1/4">
            <div class="rounded-lg overflow-hidden shadow-xl max-w-sm mx-auto">
              <img
                :src="movie.Poster"
                :alt="movie.Title"
                class="w-full"
              />
            </div>
            <div class="mt-4 bg-white rounded-lg p-4 text-center transform hover:scale-105 transition-transform duration-300 max-w-sm mx-auto">
              <img
                src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg"
                alt="Disney+"
                class="w-16 mx-auto mb-2"
              />
              <div class="text-lg font-medium mb-2">Now Streaming</div>
              <button class="w-full bg-[#0D253F] text-white py-2 rounded-lg font-medium hover:bg-[#01B4E4]">
                Watch Now
              </button>
            </div>
          </div>

          <!-- Movie Details -->
          <div class="lg:w-2/3 xl:w-3/4 text-white">
            <h1 class="text-4xl font-bold mb-2 text-shadow">
              {{ movie.Title }}
              <span class="text-gray-300">({{ movie.Year }})</span>
            </h1>

            <div class="flex flex-wrap gap-4 mb-6 text-sm">
              <span class="border border-gray-400 px-1 rounded">{{ movie.Rated }}</span>
              <span>{{ movie.Released }}</span>
              <span>•</span>
              <span>{{ movie.Genre }}</span>
              <span>•</span>
              <span>{{ movie.Runtime }}</span>
            </div>

            <!-- Actions -->
            <div class="flex flex-col sm:flex-row items-start sm:items-center gap-6 mb-8">
              <div class="flex items-center gap-4">
                <div class="relative w-16 h-16">
                  <svg class="w-full h-full transform -rotate-90 drop-shadow-glow">
                    <circle
                      cx="32"
                      cy="32"
                      r="28"
                      stroke-width="4"
                      stroke="#204529"
                      fill="none"
                    />
                    <circle
                      cx="32"
                      cy="32"
                      r="28"
                      stroke-width="4"
                      stroke="#21d07a"
                      fill="none"
                      :stroke-dasharray="175.93"
                      :stroke-dashoffset="175.93 - (175.93 * parseFloat(movie.imdbRating) / 10)"
                      class="transition-all duration-1000"
                    />
                  </svg>
                  <div class="absolute inset-0 flex items-center justify-center font-bold text-white">
                    {{ Math.round(parseFloat(movie.imdbRating) * 10) }}<span class="text-sm">%</span>
                  </div>
                </div>
                <div class="flex flex-col items-start">
                  <div class="text-lg font-bold">User Score</div>
                  <div class="flex items-center gap-1">
                    <span class="text-2xl">🎬</span>
                    <span class="text-2xl">👍</span>
                    <span class="text-2xl">⭐</span>
                  </div>
                </div>
              </div>

              <div class="flex flex-wrap items-center gap-4">
                <button class="w-10 h-10 bg-[#0D253F] rounded-full flex items-center justify-center hover:bg-[#01B4E4] transition-all duration-200 hover:scale-110">
                  <List class="w-5 h-5" />
                </button>
                <button class="w-10 h-10 bg-[#0D253F] rounded-full flex items-center justify-center hover:bg-[#01B4E4] transition-all duration-200 hover:scale-110">
                  <Heart class="w-5 h-5" />
                </button>
                <button class="w-10 h-10 bg-[#0D253F] rounded-full flex items-center justify-center hover:bg-[#01B4E4] transition-all duration-200 hover:scale-110">
                  <Bookmark class="w-5 h-5" />
                </button>
                <button class="w-10 h-10 bg-[#0D253F] rounded-full flex items-center justify-center hover:bg-[#01B4E4] transition-all duration-200 hover:scale-110">
                  <Star class="w-5 h-5" />
                </button>
                <button class="flex items-center gap-2 bg-gradient-to-r from-[#01B4E4] to-[#0D253F] hover:from-[#0D253F] hover:to-[#01B4E4] px-4 py-2 rounded-lg transition-all duration-300">
                  <Play class="w-5 h-5" />
                  Play Trailer
                </button>
              </div>
            </div>

            <div v-if="movie.Plot" class="italic text-gray-300 text-lg mb-6">{{ movie.Plot }}</div>

            <div class="mb-8">
              <h3 class="text-xl font-semibold mb-2">Overview</h3>
              <p class="text-gray-300 leading-relaxed">{{ movie.Plot }}</p>
            </div>

            <!-- Credits -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-x-12 gap-y-6">
              <div>
                <h4 class="font-semibold">{{ movie.Director }}</h4>
                <p class="text-gray-400">Director</p>
              </div>
              <div>
                <h4 class="font-semibold">{{ movie.Writer }}</h4>
                <p class="text-gray-400">Writer</p>
              </div>
              <div>
                <h4 class="font-semibold">{{ movie.Actors }}</h4>
                <p class="text-gray-400">Actors</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Search, Plus, List, Heart, Bookmark, Star, Play, Menu } from 'lucide-vue-next'

interface Movie {
  Title: string
  Year: string
  Rated: string
  Released: string
  Runtime: string
  Genre: string
  Director: string
  Writer: string
  Actors: string
  Plot: string
  Poster: string
  Ratings: Array<{ Source: string; Value: string }>
  imdbRating: string
}

const movie = ref<Movie | null>(null)

onMounted(async () => {
  try {
    const response = await fetch('http://www.omdbapi.com/?i=tt3896198&apikey=d2132124')
    movie.value = await response.json()
  } catch (error) {
    console.error('Error fetching movie data:', error)
  }
})
</script>

<style scoped>
@keyframes fillCircle {
  from {
    stroke-dashoffset: 175.93;
  }
}

circle:nth-child(2) {
  animation: fillCircle 1.5s ease-out forwards;
}

.text-shadow {
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

.drop-shadow-glow {
  filter: drop-shadow(0 0 8px rgba(33, 208, 122, 0.6));
}
</style>