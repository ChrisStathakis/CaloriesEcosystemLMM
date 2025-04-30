import { StyleSheet } from "react-native";



const baseStyle = StyleSheet.create({
    container: {
        flex: 1,

    },
    div:{
        height: "10%",
        backgroundColor: "#e4ffce",
        flex: 1,
        margin: "3%",
        borderRadius: 10,
        borderWidth: 1,
        padding: "2%",
    },
    header: { 
        height: "15%",
        backgroundColor:"skyblue",
        flex: 1
    },
    baseButton: {
        color: 'white',
        backgroundImage: 'blue'

    },
    text_info: {
        fontSize: 30,
        fontWeight: 500,
        textAlign: 'left',
        textDecorationLine: "underline",
        marginBottom: "1%"
    }
}
)

export default baseStyle;