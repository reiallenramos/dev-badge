<template lang="pug">
  div.text-center
    h6 ...or choose from handpicked palettes
    template(v-for="item in palette")
      button(:style="'background-color: ' + item.c[0] + '; color: ' + item.c[1]"
              @click="use(item)") {{ item.name }}
</template>

<script>
import { palette } from '../palette'
import Logo from './Logo'

export default {
  data() {
    return {
      palette: palette,
      current: '',
      primary: true
    }
  },
  components: {
    'logo': Logo
  },
  props: ['usePalette'],
  methods: {
    use(palette) {
      let bg = palette.c[0];
      let text = palette.c[1];
      if (this.current == palette.name && this.primary) {
        bg = palette.c[1];
        text = palette.c[0];
        this.primary = false;
      } else {
        this.current = palette.name;
        this.primary = true;
      }
      this.usePalette(bg, text);
    }
  }
}
</script>

<style scoped>
button {
  margin-right: 8px;
}

.text-center {
  text-align: center;
}
</style>
