import { View, Text, TextInput, Button } from "react-native";
import React, { useState } from "react";
import baseStyle from "../../components/styles/baseStyles";
import ProfileBox from "@/components/ui_components/profile_box";


export default function SettingsScreen() {
    const [age, setAge] = useState(0);
    const [weight, setWeight] = useState(0);

    return (
        <View style={baseStyle.container}>
           <View style={baseStyle.div}>
                <ProfileBox/>
                
           </View>
           <View style={baseStyle.div}>
                <Text style={baseStyle.text_info}>Edit Profile: </Text>
                <TextInput
                    placeholder="Weight"
                    value={weight.toString()}
                    onChangeText={setWeight}
                />
            </View>
            
        </View>

    )
}