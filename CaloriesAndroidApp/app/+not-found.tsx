import { Stack } from "expo-router";
import { View, StyleSheet } from "react-native";

import { Link } from "expo-router";


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
});

export default function NotFoundScreen() {
    return (
        <>
        <Stack.Screen options={{ title: "Not Found" }} />
        <View style={styles.container}>
            <Link href="/" style={styles.text}>This screen doesn't exist.</Link>
        </View>
        </>
    )
}

