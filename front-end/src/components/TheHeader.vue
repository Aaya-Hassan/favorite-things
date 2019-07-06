<template>
  <nav>
    <div>
      <router-link :to="{ name: 'home' }">
        Favorite
      </router-link>
      <ul>
        <li>
          <router-link
                  active-class="active"
                  exact
                  :to="{ name: 'home' }"
          >
            Home
          </router-link>
        </li>
        <li>
          <router-link
                  active-class="active"
                  :to="{ name: 'favorite-edit' }"
          >
            <i class="ion-compose"></i>&nbsp;New Favorite
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'
  export default {
    name: 'RwvHeader',
    computed: {
      ...mapGetters(['currentUser'])
    }
  }
</script>
