import { fetch_profile } from '@/data/users/profile';
import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import axiosInstance from '@/data/axiosInstanceHTTP';



export  function HomepageBodyView() {
    const [profile, setProfile] = useState({});


    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const data = await fetch_profile(); // Replace '/profile' with your API endpoint
                setProfile(data);
            } catch (err) {
                
            } finally {
                
            }
        };

        fetchProfile();
    }, []);

}