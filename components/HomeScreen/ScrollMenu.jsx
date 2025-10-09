import React from 'react';
import { TouchableOpacity, Text, StyleSheet, View } from 'react-native';
import { useRouter } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

const ScrollMenu = () => {
  const router = useRouter();

  const menus = [
    { title: 'Pinjaman Terkini', route: '/page/PinjamanTerkini', icon: 'book-outline' },
    { title: 'Judul Tertandai', route: '/page/JudulDitandai', icon: 'bookmark-outline' },
    // { title: 'Keranjang Judul Anda', route: '/page/KeranjangJudul', icon: 'cart-outline' },
    { title: 'Sejarah Peminjaman', route: '/page/SejarahPeminjaman', icon: 'time-outline' },
    { title: 'Akun Saya', route: '/page/AkunSaya', icon: 'person-outline' },
  ];

  return (
    <View style={styles.container}>
      {menus.map((menu, index) => (
        <TouchableOpacity
          key={index}
          style={styles.menuItem}
          onPress={() => router.push(menu.route)} >
          <View style={styles.iconWrapper}>
            <Ionicons name={menu.icon} size={24} color="#fff" />
          </View>
          <View style={styles.menuTextWrapper}>
            {menu.title.split(' ').map((word, i) => (
              <Text key={i} style={styles.menuText}>{word}</Text>
            ))}
          </View>
        </TouchableOpacity>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    paddingVertical: 10,
  },
  menuItem: {
    flexDirection: 'column',
    alignItems: 'center',
    paddingVertical: 10,
    marginHorizontal: 8,
  },
  iconWrapper: {
    backgroundColor: '#5D7BF4',
    padding: 15,
    borderRadius: 10,
    marginBottom: 5,
  },
  menuTextWrapper: {
    alignItems: 'center',
  },
  menuText: {
    fontSize: 14,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#333',
    lineHeight: 18,
  },
});

export default ScrollMenu;