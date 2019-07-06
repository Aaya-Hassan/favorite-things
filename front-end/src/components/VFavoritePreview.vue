<template>
  <div class="article-preview">
    <router-link :to="articleLink" class="preview-link">
      <h1 v-text="favorite.title" />
      <p v-text="favorite.description" />
      <button class="btn btn-outline-danger btn-sm" @click="deleteFavorite">
        <i class="ion-trash-a"></i> <span>&nbsp;Delete Favorite</span>
      </button>
      <router-link class="btn btn-sm btn-outline-secondary" :to="editArticleLink">
        <i class="ion-edit"></i> <span>&nbsp;Edit Favorite</span>
      </router-link>
    </router-link>
  </div>
</template>

<script>


  export default {
    name: "RwvArticlePreview",
    components: {
    },
    props: {
      favorite: { type: Object, required: true }
    },
    computed: {
      articleLink() {
        return {
          name: "favorite",
        };
      },
      editArticleLink() {
        return { name: "favorite-edit", params: { slug: this.favorite.id } };
      },
    },
    methods: {
      async deleteFavorite() {
      }
    }
  };
</script>
