import { Stack, Tabs } from "expo-router";
import TabLayout from "./(tabs)/_layout";


export default function RootLayout() {
  return (
    <Stack>
      <TabLayout />     
    </Stack>
  );
}
