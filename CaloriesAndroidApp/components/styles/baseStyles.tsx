import { StyleSheet } from "react-native";



const baseStyle = StyleSheet.create({
    container: {
        flex: 1,
        width: "100%",

    },
    box: {
        backgroundColor: "#E8F5E9",
        flex: 1,
        padding: 16,
        margin: 16,
        borderWidth: 1,
        borderColor: "#4CAF50",
        borderRadius: 12,
    },
    box_title: {
        fontSize: 24,
        fontWeight: "bold",
        color: "#388E3C",
        marginBottom: 16,
        borderBottomColor: "#4CAF50",
        paddingBottom: 8
    },
    box_row: {
        flexDirection: "row",
        paddingVertical: 8,
    },
    box_label: {
        fontSize: 18,
        fontWeight: "bold",
        color: "#388E3C",
        width: "100%",
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
    },
    table_row: {
        flexDirection: 'row',
        borderBottomWidth: 1,
        borderBottomColor: '#ccc',
        paddingVertical: 10,
    },
    table_cell: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    table_header: {
        backgroundColor: '#ddd',
        fontWeight: 'bold',
    },
}
)

export default baseStyle;