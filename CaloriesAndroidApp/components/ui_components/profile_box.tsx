import React from "react";
import { View, Text, StyleSheet } from "react-native";


const ProfileBox = () => {

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Profile</Text>

            <View style={styles.infoRow}>
                <Text style={styles.label}>Age: 39</Text>
            </View>

            <View style={styles.infoRow}>
                <Text style={styles.label}>Weight: 84</Text>
            </View>

            <View style={styles.infoRow}>
                <Text style={styles.label}>Height: 175</Text>
            </View>

            <View style={styles.infoRow}>
                <Text style={styles.label}>Activity lvl: Medium</Text>
            </View>

        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: "#E8F5E9",
        borderRadius: 12,
        padding: 16,
        margin: 16,
        borderWidth: 1,
        borderColor: "#4CAF50",
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
        color: "#388E3C",
        marginBottom: 16,
        borderBottomColor: "#4CAF50",
        paddingBottom: 8
    },
    infoRow: {
        flexDirection: "row",
        paddingVertical: 8,
    },
    label: {
        fontSize: 18,
        fontWeight: "bold",
        color: "#388E3C",
        width: "100%",
    }
})

export default ProfileBox;