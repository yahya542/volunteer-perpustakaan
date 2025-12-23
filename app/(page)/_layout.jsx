import { Tabs } from "expo-router";
import TabBar from "../../components/tab-bar/TabBar"; 

export default function TabLayout() {
  return (
    <Tabs tabBar={(props) => <TabBar {...props} />}>
      <Tabs.Screen
        name="HomePage"
        options={{ title: "Home", headerShown: false }}
      />
      <Tabs.Screen
        name="JudulDitandai"
        options={{ title: "Ditandai", headerShown: false }}
      />
      <Tabs.Screen
        name="PinjamanTerkini"
        options={{ title: "Pinjaman", headerShown: false }}
      />
      <Tabs.Screen
        name="SejarahPeminjaman"
        options={{ title: "Sejarah", headerShown: false }}
      />
      <Tabs.Screen
        name="AkunSaya"
        options={{ title: "Akun", headerShown: false }}
      />
    </Tabs>
  );
}