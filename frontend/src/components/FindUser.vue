<template lang="pug">
  div
    .row
      .twelve.columns
        template(v-if="!isLoadingUser")
          label(for="username") or
          input#username.u-half-width(type="text" placeholder="Find username"
                                      v-model="username")
          button(@click="findUser(username)" :disabled="username == ''") Go
        template(v-else)
          label Loading...
</template>

<script>
export default {
  data() {
    return {
      username: ''
    }
  },
  props: ['findUser', 'isLoadingUser']
}
</script>

<style scoped>
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>