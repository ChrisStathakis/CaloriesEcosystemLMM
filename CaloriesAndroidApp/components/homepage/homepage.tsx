import { fetch_homepage_data, fetch_profile } from '@/data/users/profile';
import React, { useState, useEffect } from 'react';
import { View, Text, Pressable, Button, ScrollView, SafeAreaView } from 'react-native';
import axiosInstance from '@/data/axiosInstanceHTTP';
import baseStyle from '../styles/baseStyles';


const profile_dummy_data = {
    username: 'Loading...'
}


const homepage_dummy_data = {
    category_data:[{"title":"Loading...", "calories": 0, "protein": 0, "carbs": 0, "fat": 0}],
}


export  function HomepageBodyView() {
    const [profile, setProfile] = useState({profile_dummy_data});
    const [homepageData, setHomepageData] = useState({homepage_dummy_data});

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const data = await fetch_profile(); // Replace '/profile' with your API endpoint
                setProfile(data);
            } catch (err) {
                
            } finally {
                
            }
        };

        const fetchHomepageData = async () => {try {const data = await fetch_homepage_data(); setHomepageData(data);} catch {}}
        fetchHomepageData();
        fetchProfile();
        console.log("homepageData", homepageData);
    }, []);
    

    return (
        <SafeAreaView>
        <ScrollView style={baseStyle.container}>
            <Text style={baseStyle.box_title}>Welcome {profile.username}</Text>
            <View style={{flex: 1, flexDirection: "row"}}>
                <View style={baseStyle.box}>
                    <Text style={baseStyle.box_label}>
                        Today Calories: {homepageData.today_calories} 
                    </Text> 
                    <Text style={baseStyle.box_label}>
                        Total Protein: 0
                    </Text>    
                </View>
                <View style={baseStyle.box}> 
                    <Text style={baseStyle.box_label}>
                        Average Calories (Month): {homepageData.this_month_calories} 
                    </Text> 
                    <Text style={baseStyle.box_label}>
                        Average Calories (7 last days):  {homepageData.last_7_days_calories} 
                    </Text> 
                </View>
            </View> 

            <View style={baseStyle.box}>
                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_title}>USER DATA  </Text>     
                </View>
                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_label}>Suggested Calories: {profile.calories} </Text> 
                    <Text style={baseStyle.box_label}>BMR: {profile.bmr}  </Text>     
                   
                </View>
                <View style={baseStyle.box_row}>
                <Text style={baseStyle.box_label}>AGE: {profile.age}  </Text>
                <Text style={baseStyle.box_label}>Activity LvL: {profile.activity_lvl} </Text>                       
                </View>

                <View style={baseStyle.box_row}>
                    <Text style={baseStyle.box_label}>Height: {profile.height} cm</Text> 
                    <Text style={baseStyle.box_label}>Weight: {profile.weight}  kg</Text>               
                </View>

            </View>

            <View style={baseStyle.box}>
                <Text style={baseStyle.box_title}> DATA PER CATEGORY </Text>
                <View style={[baseStyle.table_row, baseStyle.table_header]}>
                    <Text style={baseStyle.table_cell}>Category</Text>
                    <Text style={baseStyle.table_cell}>Calories</Text>
                    <Text style={baseStyle.table_cell}>Protein</Text>
                    <Text style={baseStyle.table_cell}>Carbs</Text>
                    <Text style={baseStyle.table_cell}>Fats</Text>
                </View>
                {homepageData.category_data !== undefined ?  homepageData.category_data.map((item, index) => (
                    <View key={index} style={baseStyle.table_row}>
                        <Text style={baseStyle.table_cell}>{item.title}</Text>
                        <Text style={baseStyle.table_cell}>{item.calories}</Text>
                        <Text style={baseStyle.table_cell}>{item.protein}</Text>
                        <Text style={baseStyle.table_cell}>{item.carbs}</Text>
                        <Text style={baseStyle.table_cell}>{item.fat}</Text>
                    </View>
                )):
                    <View style={baseStyle.table_row}>
                         <Text style={baseStyle.table_cell}>No data</Text>
                    </View>
                }
            </View>

            <View style={baseStyle.box}>
                <Button title="TODAY DATA" onPress={() => console.log("Add Food")} />
            </View>
        </ScrollView>
        </SafeAreaView>
    );

}