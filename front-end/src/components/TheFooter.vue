<template>
  <footer>
    <div>
      <router-link :to="{ name: 'home', params: {} }">
      Favorite
      </router-link>
      <span class="attribution">
        Your favorite place for your favorite things
        <a rel="noopener noreferrer" target="blank"
          ></a>
      </span>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'RwvFooter'
}
</script>
