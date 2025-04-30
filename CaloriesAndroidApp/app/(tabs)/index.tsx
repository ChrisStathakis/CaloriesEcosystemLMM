import { checkIfAuthenticated } from "@/data/users";
import { Link } from "expo-router";
import { Text, View, StyleSheet } from "react-native";
import React , { useState, useEffect } from "react";
import { IS_AUTHENTICATED_FALSE, IS_AUTHENTICATED_TRUE } from "@/data/actionTypes";
import LoginScreen from "@/components/extras/login_screen";

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


  
  return (
    <View style={styles.container}>

      {isAuthenticated === IS_AUTHENTICATED_FALSE ? <LoginScreen /> : <Text style={styles.text}>Homepage {isAuthenticated} {IS_AUTHENTICATED_TRUE}</Text>}
    </View>
  );
}
