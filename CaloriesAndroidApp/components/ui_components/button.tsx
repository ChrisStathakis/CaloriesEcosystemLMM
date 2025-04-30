import { StyleSheet, View, Pressable, Text } from "react-native";


type Props = {
    title: string;  
    theme? : "primary";
    onPress: () => void;
}

export default function MyButton({title, theme, onPress }: Props) {
    if (theme === "primary") {
        return(
            <View style={styles.containerPrimary}>
                <Pressable style={styles.button} onPress={() => onPress()}>
                    
                    <Text style={{color: "#ffd33d", fontSize: 20, fontWeight: "bold"}}>{title}</Text>
                </Pressable>
            </View>
        )
    }

    return (
        <Pressable style={styles.button} onPress={() => onPress()}>
            <Text style={{color: "#fff", fontSize: 20, fontWeight: "bold"}}>{title}</Text>
        </Pressable>
    )

}



const styles = StyleSheet.create({
    containerPrimary: {
        borderWidth:4,
        borderColor: "#ffd33d",
        borderRadius: 18
    },
    button: {
        borderRadius:10,
        width: "100%",
        height: "100%",
        alignItems: "center",
        justifyContent: "center",
        flexDirection: "row",
    },
});