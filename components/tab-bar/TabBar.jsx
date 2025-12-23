import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

const TabBar = ({ state, navigation }) => {
  const activeColor = '#5a3fd1';
  const inactiveColor = '#6d6a75';

  const icons = {
    HomePage: require('../../assets/icons/Home.png'),
    JudulDitandai: require('../../assets/icons/Bookmark.png'),
    PinjamanTerkini: require('../../assets/icons/Alarm.png'),
    SejarahPeminjaman: require('../../assets/icons/Time.png'),
    AkunSaya: require('../../assets/icons/Account.png'),
  };

  const labels = {
    HomePage: 'Home',
    JudulDitandai: 'Ditandai',
    PinjamanTerkini: 'Pinjaman',
    SejarahPeminjaman: 'History',
    AkunSaya: 'Akun',
  };

  return (
    <View style={styles.container}>
      {state.routes.map((route, index) => {
        const isFocused = state.index === index;

        const onPress = () => {
          const event = navigation.emit({
            type: 'tabPress',
            target: route.key,
            canPreventDefault: true,
          });

          if (!isFocused && !event.defaultPrevented) {
            navigation.navigate(route.name);
          }
        };

        return (
          <TouchableOpacity
            key={route.key}
            style={styles.tabItem}
            onPress={onPress}
            activeOpacity={0.7}
          >
            <Image
              source={icons[route.name]}
              style={{
                width: 40,
                height: 40,
                tintColor: isFocused ? activeColor : inactiveColor,
              }}
            />

            <Text
              style={{
                marginTop: 4,
                fontSize: 12,
                fontWeight: isFocused ? '600' : '400',
                color: isFocused ? activeColor : inactiveColor,
              }}
            >
              {labels[route.name]}
            </Text>
          </TouchableOpacity>
        );
      })}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    bottom: 25,
    left: 20,
    right: 20,
    flexDirection: 'row',
    backgroundColor: '#ece8ff',
    paddingVertical: 12,
    borderRadius: 28,
    borderCurve: 'continuous',
    shadowColor: '#000',
    shadowOpacity: 0.15,
    shadowOffset: { width: 0, height: 5 },
    shadowRadius: 12,
    elevation: 5,
  },

  tabItem: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default TabBar;
