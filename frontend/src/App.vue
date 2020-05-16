<template lang="pug">
  #app.container
    #content
      section.row.center
        .six.columns
          .card
            logo(:bgColor="bgColor" :textColor="textColor")
      section.row.center
        .six.columns
          .currentHexContainer
            #currentBg
              span.hexLabel background&nbsp;
              span.currentHex {{ bgColor }}
            #currentText
              span.hexLabel text&nbsp;
              span.currentHex {{ textColor}}
      section.randomize-container
        button.button-primary(@click="randomize") Randomize!
      section.find-user-container
        find-user(:findUser="handleFindUser" :isLoadingUser="isLoadingUser")
      section.row.palette-container
        .twelve.columns
          palette(:usePalette="handleUsePalette")
    footer
      section.row.disclaimer-container
        .twelve.columns
          disclaimer
</template>

<script>
import Logo from './components/Logo'
import randomColor from 'randomcolor'
import Palette from './components/Pallete'
import Disclaimer from './components/Disclaimer'
import FindUser from './components/FindUser'

let apiURL = process.env.VUE_APP_API_URL

export default {
  name: 'App',
  data() {
    return {
      bgColor: '',
      textColor: '',
      isLoadingUser: false,
    }
  },
  components: {
    'logo': Logo,
    'palette': Palette,
    'disclaimer': Disclaimer,
    'find-user': FindUser
  },
  methods: {
    randomize() { this.changeBgColor(); this.changeTextColor() },
    changeBgColor() { this.bgColor = randomColor() },
    changeTextColor() { this.textColor = randomColor() },
    handleUsePalette(bg, text) { this.bgColor = bg; this.textColor = text; },
    handleFindUser(username) {
      this.isLoadingUser = true;
      this.axios.get(`${apiURL}/${username}`).then((response) => {
        this.bgColor = response.data.bg;
        this.textColor = response.data.color;
        this.isLoadingUser = false;
      }).catch(() => {
        alert(`${username} not found!`)
        this.isLoadingUser = false;
      })
    }
  },
  created() {
    this.randomize();
  }
}
</script>

<style>
#app {
  font-family: Raleway, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#content {
  margin: 10px 0px;
  border-radius: 3px;
}

footer {
  border-top: 1px solid #eee;
  text-align: center;
}

.card {
  border-radius: 10px;
  padding: 15px;
  text-align: center;
}

.currentHexContainer {
  display: flex;
}

#currentBg, #currentText {
  flex: 1;
  text-align: center;
}

.hexLabel {
  font-size: 1rem;
}

.currentHex {
  font-size: 2rem;
}

.randomize-container, .find-user-container {
  text-align: center;
}

.center {
  display: flex;
  justify-content: center;
}

section {
  padding: 1rem 0 0 0;
}
</style>
