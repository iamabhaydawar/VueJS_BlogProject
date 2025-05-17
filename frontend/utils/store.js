
const store = new Vuex.Store({
    state: {
        //like data shared b/w various components
        auth_token:null,
        role:null,
        loggedIn:false, //just for clarity
        user_id:null,
    },
        mutations:{ 
        //functions that change the state\\
        setUser(state){
            try{
                if(JSON.parse(localStorage.getItem('user'))){
                    const user = JSON.parse(localStorage.getItem('user'));
                    state.auth_token=user.token;
                    state.role=user.role;
                    state.loggedIn=true;
                    state.user_id=user.id;
                }
            } catch{ 
                console.log('not Logged in')
        
            }    
        },
        logout(state){
            state.auth_token=null;
            state.role=null;
            state.loggedIn=false; 
            state.user_id=null;
            localStorage.removeItem('user')
        }

    },
    actions:{
        //actions commit mutations,can be async

    }
})
store.commit('setUser')
export default store;