export default {
    template:`
    <div>
        <input placeholder="email" v-model="email"/>
        <input placeholder="roles" v-model="roles"/>
        <input placeholder="password" v-model="password"/>

        <button class='btn btn-primary' @click="registerLogin">Register</button>
    </div>
    `,
    data(){
        return{
            email:null,
            roles:null,
            password:null,
         }
        },
        methods: {
        async registerLogin() {  
            const res = await fetch(location.origin+'/register', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: this.email,
                    roles:this.roles,
                    password: this.password,
                })
            });
            if (res.ok) {
                console.log("You are successfully registered");
            }
        }
    }
}