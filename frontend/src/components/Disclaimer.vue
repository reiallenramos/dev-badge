<template lang="pug">
  div
    p
      a.icon-link(href="https://github.com/reiallenramos" title="Follow me on Github!" target="_blank")
        i.bx.bxl-github
      a.icon-link(href="https://dev.to/brand" title="DEV Brand Guidelines" target="_blank")
        img.dev-ecosystem-logo(src="../assets/dev-ecosystem.png" alt="Dev Ecosystem Logo")
    p
      h6 This is an unofficial DEV app. I do not own the DEV brand nor the DEV logo.

</template>

<style scoped>
.icon-link {
  padding: 10px;
}

.bxl-github {
  font-size: 28px;
  color: #222;
}

.dev-ecosystem-logo {
  height: 25px;
}

p {
  margin-bottom: 0;
}

h6 {
  font-size: 10px;
}
</style>