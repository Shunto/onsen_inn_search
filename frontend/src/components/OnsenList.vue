<template>
  <div id='list'>
    <v-container fluid grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex xs12>
          <v-layout column wrap>

            <v-flex xs12>
              <v-layout column wrap>
                <v-flex xs6>
                  <img class="onei" :src="require('../assets/images/0/download20190702162626.png')"/>
                </v-flex>
                <v-flex xs6>
                  好きなの選んでね!
                </v-flex>
              </v-layout>
            </v-flex>

            <v-flex xs6>
              <v-card>
                <v-list>
                  <v-list-tile v-for="(item, index) in items[page-1]" :key="item.inn_name" @click="goToOnsenPage(item.id)" >
                    <v-list-tile-content>
                      <v-list-tile-title v-text="(index+1+(page-1)*10) + '位: ' + item.inn_name"></v-list-tile-title>
                      <v-list-tile-sub-title v-text="item.vote_score + '票'"></v-list-tile-sub-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>
                <v-pagination v-model="page" :length="pagesize" ></v-pagination>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
  name: 'OnsenList',
  data () {
    return {
      category: 0,
      page: 1,
      ordering: '-vote_score',
      count: 0,
      pagesize: 0,
      items: []
    }
  },

  created () {
    if (this.$route.query.category != null) {
      this.category = this.$route.query.category
    }

    if (this.$route.query.page != null) {
      this.page = this.$route.query.page
    }

    if (this.$route.query.count != null) {
      this.count = this.$route.query.count
      this.pagesize = parseInt(this.count/10)+1
      console.log("got query")
    }

    console.log("Called")
    console.log(this.category)
    console.log(this.page)
    console.log(this.count)
    console.log(this.pagesize)

    //for (  var i = 0;  i < 6;  i++  ) {
    for (  var i = 0;  i < this.pagesize;  i++  ) {
      axios.get('http://localhost:8000/api/onsen_inns/', {
        params: {
          category: this.category,
          ordering: this.ordering,
          page: i+1,
        },
      })
        .then(response => {
          console.log(response.data.results)
          this.items.push(response.data.results)
        })
        .catch(err => {
          console.error(err)
        })
    }
  },

  methods:{
    goToOnsenPage : function (itemid) {
      this.$router.push({ name: 'Onsen', params: { id: itemid }, query: { count: this.count }})
    }
  },
}
</script>

<style scoped>
h1 {
  font-weight: normal;
  font-size: 32px;
}

</style>
