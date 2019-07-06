<template>
  <div>
    <div>
      <div v-if="favorites.length === 0" class="article-preview">
        No favorites are here... yet.
      </div>
      <RwvFavoritePreview
        v-for="(favorite, index) in favorites"
        :favorite="favorite"
        :key="favorite.favorite + index"
      />
    </div>
  </div>
</template>

<script>
import RwvFavoritePreview from "./VFavoritePreview";
import axios from 'axios'

export default {
   name: "RwvFavoriteList",
    components: {
    RwvFavoritePreview
  },
  data: () => {
    return {
      favorites: []
    }
  },

  created () {
    this.getFavorites()
  },

  methods: {
    getFavorites () {
      axios.get(
        '/favorites/'
      ).then(response => {
        this.favorites = response.data
      }).catch(error => {
        console.log(error)
      })
    }
  }

};
</script>
