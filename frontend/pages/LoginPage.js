export default {
    template:`
    <div>
        <input placeholder="username" v-model="username"/>
        <input placeholder="email" v-model="email"/>
        <input placeholder="password" v-model="password"/>
        <button class='btn btn-primary' @click="submitLogin">Login</button>
    </div>
    `,
    data(){
        return{
            username:null,
            email:null,
            password:null,
         }
        },
        methods: {
        async submitLogin() {  
            const res = await fetch(location.origin+'/login', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: this.username,
                    email: this.email,
                    password: this.password
                })
            });
            if (res.ok) {
                const data = await res.json();
                console.log("we are logged in");

                localStorage.setItem('user',JSON.stringify(data)) //this stores user data in local Storage
                this.$store.commit('setUser') //takes data from the local storage  and set's the vuex
                this.$router.push('/feed') //this is the router object that pushes the data into /feed
            }
        }
    }
}