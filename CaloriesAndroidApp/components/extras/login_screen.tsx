import { View, Text, TextInput, StyleSheet, Pressable } from 'react-native';
import React, { useState } from 'react';

import { fetchAuthToken } from '../../data/users';



export default function LoginScreen() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    const handleLogin = async () => {
        const data = {username, password};
        console.log("data", data);
        fetchAuthToken(data);
       
        
    }



    return (
        <View style={styles.container}>
            <Text>Login Screen</Text>
            <View style={styles.form_group}>
                <Text>Username</Text>
                <TextInput 
                    value={username}
                    onChangeText={(text)=> setUsername(text)}
                    placeholder='Username'
                />
            </View>

            <View style={styles.form_group}>
                <Text>Password</Text>
                <TextInput 
                    value={password}
                    onChangeText={(text)=> setPassword(text)}
                    placeholder='Password'
                    secureTextEntry
                 />
            </View>

            <Pressable onPress={handleLogin}>
                <Text>Login</Text>
            </Pressable> 
        </View>
    )

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        marginTop: '20%',
        marginBottom: '25%',
        width:"80%",
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#e9e5cd',

    },
    form_group: {
        width: '100%',
        marginBottom: '10%',
        borderWidth: 1,
        borderColor: '#000',
        padding: 10,
        borderRadius: 5,
    },
    button_text: {
        color: 'black'
    }
        
    
})