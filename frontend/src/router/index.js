import Vue from 'vue'
import Router from 'vue-router'
import OnsenHome from '@/components/OnsenHome'
import Onsen from '@/components/Onsen'
import Tinder from '@/components/Tinder'
import OnsenList from '@/components/OnsenList'
import Category from '@/components/Category'
import Login from '@/components/Login'
import Signup from '@/components/Signup'
import NotFound from '@/components/NotFound'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: OnsenHome,
    },
    {
      path: '/onsen/:id',
      name: 'Onsen',
      component: Onsen,
    },
    {
      path: '/tinder',
      component: Tinder,
    },
    {
      path: '/onsenlist',
      name: 'OnsenList',
      component: OnsenList,
    },
    {
      path: '/category',
      name: 'Category',
      component: Category,
    },
    {
      path: '/login',
      component: Login,
    },
    {
      path: '/signup',
      component: Signup,
    },
    {
      path: '*',
      component: NotFound,
    },
  ],
})
