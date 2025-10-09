import { StyleSheet, Text, View, FlatList, Image } from "react-native";
import React, { useState, useEffect } from 'react';

const ComponentJudulDitandai = () => {
  const [bookmarks, setBookmarks] = useState([]);

  useEffect(() => {
    fetchBookmarks();
  }, []);

  const fetchBookmarks = async () => {
    try {
      const response = await fetch('https://0b8763b66148.ngrok-free.app/api/bookmarks/');
      const data = await response.json();
      setBookmarks(data);
    } catch (error) {
      console.error('Error fetching bookmarks:', error);
      setBookmarks([]);
    }
  };

  const renderBookmark = ({ item }) => (
    <View style={styles.bookmarkItem}>
      <Image source={{ uri: item.cover }} style={styles.cover} />
      <View style={styles.info}>
        <Text style={styles.title}>{item.title}</Text>
        <Text style={styles.author}>by {item.author}</Text>
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.titleText}>Judul Tertandai Milik Saya</Text>
      </View>
      <View style={styles.countContainer}>
        <Text>{bookmarks.length} daftar judul saat ini</Text>
      </View>
      {bookmarks.length === 0 ? (
        <View style={styles.noData}>
          <Text>Tidak ada data</Text>
        </View>
      ) : (
        <FlatList
          data={bookmarks}
          keyExtractor={(item) => item.id.toString()}
          renderItem={renderBookmark}
          contentContainerStyle={styles.list}
          showsVerticalScrollIndicator={true}
        />
      )}
    </View>
  );
};

export default ComponentJudulDitandai;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: '100%',
  },
  titleContainer: {
    marginTop: 20,
    alignItems: "flex-start",
    width: "100%",
    paddingLeft: 20,
  },
  titleText: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#344175",
  },
  countContainer: {
    marginTop: 20,
    alignItems: "flex-start",
    width: "100%",
    paddingLeft: 20,
  },
  noData: {
    marginTop: 20,
    alignItems: "center",
    justifyContent: "center",
  },
  list: {
    paddingHorizontal: 20,
    paddingTop: 20,
  },
  bookmarkItem: {
    flexDirection: 'row',
    backgroundColor: "#fff",
    padding: 10,
    borderRadius: 10,
    marginBottom: 10,
    alignItems: 'center',
  },
  cover: {
    width: 80,
    height: 100,
    borderRadius: 8,
    marginRight: 10,
  },
  info: {
    flex: 1,
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  author: {
    fontSize: 14,
    color: '#666',
  },
});
