import React, { useState, useEffect } from 'react';
import { View, Text, Image, FlatList, StyleSheet } from 'react-native';

const BukuFavoritPage = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetchFavorites();
  }, []);

  const fetchFavorites = async () => {
    try {
      const response = await fetch('https://api.example.com/books/favorites');
      const data = await response.json();
      setBooks(data);
    } catch (error) {
      console.error('Error fetching favorites:', error);
      setBooks([]);
    }
  };

  const renderBook = ({ item }) => (
    <View style={styles.bookItem}>
      <Image source={{ uri: item.cover }} style={styles.cover} />
      <Text style={styles.title}>{item.title}</Text>
      <Text style={styles.author}>by {item.author}</Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Buku Favorit</Text>
      <FlatList
        data={books}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderBook}
        numColumns={2}
        contentContainerStyle={styles.list}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
    textAlign: 'center',
  },
  list: {
    paddingBottom: 16,
  },
  bookItem: {
    flex: 1,
    margin: 8,
    alignItems: 'center',
  },
  cover: {
    width: 120,
    height: 147,
    borderRadius: 8,
  },
  title: {
    fontSize: 14,
    fontWeight: 'bold',
    textAlign: 'center',
    marginTop: 4,
  },
  author: {
    fontSize: 12,
    color: '#666',
    textAlign: 'center',
  },
});

export default BukuFavoritPage;