import { checkIfAuthenticated } from "@/data/users";
import { Text, View, StyleSheet } from "react-native";
import React , { useState, useEffect } from "react";
import { ACCESS_TOKEN, IS_AUTHENTICATED, IS_AUTHENTICATED_FALSE, IS_AUTHENTICATED_TRUE, REFRESH_TOKEN } from "@/data/actionTypes";
import LoginScreen from "@/components/extras/login_screen";
import { HomepageBodyView } from "@/components/homepage/homepage";
import Storage from "../../data/myStorage";


const styles = StyleSheet.create({
  container: {
   flex: 1,
   backgroundColor: "#25292e",
   alignItems: "center",
    justifyContent: "center",
  },
  text: {
    color: "#fff",
  },
  button: {
    backgroundColor: "#007AFF",
  }
});


export default function Index() {
  const [isAuthenticated, setIsAuthenticated] = useState('loading');
  

  useEffect (() => {
    const checkAuthStatus = async () => {
      const authStatus = await checkIfAuthenticated();
      if (authStatus === IS_AUTHENTICATED_TRUE) {
        setIsAuthenticated(IS_AUTHENTICATED_TRUE);
      }
      if (authStatus === IS_AUTHENTICATED_FALSE) {  
          setIsAuthenticated(IS_AUTHENTICATED_FALSE);
      }
    }
    checkAuthStatus();
    
  }, [])

  useEffect(() => {
    console.log("changed", Storage.getItem(ACCESS_TOKEN), 
    Storage.getItem(REFRESH_TOKEN),);  
  }, [Storage.getItem(IS_AUTHENTICATED)])

  
  return (
    <View style={styles.container}>

      {isAuthenticated === IS_AUTHENTICATED_FALSE ? <LoginScreen /> : 
      <HomepageBodyView />
      }
    </View>
  );
}
