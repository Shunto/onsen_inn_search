<template>
  <v-content>
    <v-container>
      <v-layout row wrap justify-space-between>
        <v-flex xs12  md6>
          <v-form v-model="valid">
            <v-text-field v-model="username" v-validate="'required'"
              data-vv-name="username" label="お名前" required>
            </v-text-field>
            <v-text-field v-validate="'required|email'" v-model="email"
              :error-messages="errors.collect('email')" label="メールアドレス"
              data-vv-as="メールアドレス" data-vv-name="email" required >
            </v-text-field>
            <v-text-field v-model="password" v-validate="'required'" type="password"
              name="password" label="パスワード" ref="password" required >
            </v-text-field>
            <!-- <v-text-field v-model="password" v-validate="'required'" type="password" name="password1" label="パスワード">-->
            <!-- </v-text-field>-->
            <!-- <v-text-field v-model="passwordConfirmation" type="password" name="password2" label="パスワード確認" v-validate=> -->
            <!-- </v-text-field>-->
              <v-btn @click="validate" :loading="loading"> サインアップ </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
  $_veeValidate: {
      validator: 'new'
  },
  data: () => ({
      valid: false,
      username: '',
      email: '',
      password1: '',
      password2: '',
      loading: false,
  }),
  methods: {
    validate() {
      this.$validator.validateAll()
      .then(x => {
        if (x && !this.loading) {
          this.loading = true
          var params = {
              username: this.username,
              email: this.email,
              password1: this.password,
              password2: this.password,
          }
          axios.post('http://localhost:8000/api/rest-auth/registration/', params)
          .then(res => {
              console.log(res)
              this.$store.commit("SET_TOKEN", res.data.key)
              this.$router.push({ path: '/tinder' })
          })
          .catch((error) => {
            console.log(params)
            console.log(error)
            this.loading = false
          })
        }
      }).catch(e => {
          console.log(e)
      })
    }
  }
}
</script>
