export default {
    template:`    
    <div>
         <router-link to='/'>Home</router-link>
         <router-link v-if='!$store.state.loggedIn' to='/login'>login</router-link>
         <router-link v-if='!$store.state.loggedIn' to='/register'>Register</router-link>

         <router-link v-if='$store.state.loggedIn && $store.state.role == "admin"'  to='/admin-dashboard'>Admin Dashboard</router-link>
         <router-link v-if='$store.state.loggedIn && $store.state.role == "user"'  to='/feed'>feed</router-link>
         <router-link v-if='$store.state.loggedIn && $store.state.role == "user"'  to='/explore'>Explore</router-link>


         <button v-if='$store.state.loggedIn'class='btn btn-dark' @click="$store.commit('logout')">Logout</button>

    </div>
    `

} 