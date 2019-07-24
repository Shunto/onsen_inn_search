<template>
  <div v-if="isLoggedIn===false">
    <v-btn large class='primary' @click='signup'> Sign Up </v-btn>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  data: () => {
    return {
      isLoggedIn: false
    }
  },
  mounted () {
    console.log(this.$store.state.token)
    if (this.$store.state.token != null) {
      console.log('You are loggedin')
      this.isLoggedIn = true
    } else {
      console.log('You are loggedout')
      this.isLoggedIn = false
    }
  },
  methods: {
    signup () {
      this.$router.push({ path: "/signup" })
    },
  }
}
</script>

<style scoped>
  h1 {
    margin: 5px 0px;
    font-size: 20px;
  }
</style>
