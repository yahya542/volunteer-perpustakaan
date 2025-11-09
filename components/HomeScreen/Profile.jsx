// import React, { useState, useEffect } from 'react';
import { View, StyleSheet, Text } from 'react-native';
import { useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

const Profile = () => {
  const [realname, setRealname] = useState('User');
  // const [imageUri, setImageUri] = useState(null);

  useEffect(() => {
    const loadRealname = async () => {
      try {
        const storedRealname = await AsyncStorage.getItem('realname');
        if (storedRealname) {
          setRealname(storedRealname);
        }
      } catch (error) {
        console.log('Error loading realname:', error);
      }
    };
    loadRealname();
  }, []);

  // useEffect(() => {
  //   const fetchProfileImage = async () => {
  //     try {
  //       const response = await fetch('https://your-backend.com/api/profile-picture');
  //       const data = await response.json();
  //       setImageUri(data.imageUrl);
  //     } catch (error) {
  //       console.error('Error fetching profile image:', error);
  //     }
  //   };

  //   fetchProfileImage();
  // }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.realnameText}>{realname}</Text>
      {/* {imageUri ? (
        <Image source={{ uri: imageUri }} style={styles.profileImage} />
      ) : (
        <View style={styles.placeholder} />
      )} */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    justifyContent: 'center',
    alignItems: 'center',
    right: 40,
    bottom: 30,
  },
  realnameText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  profileImage: {
    width: 81,
    height: 81,
    borderRadius: 40.5,
  },
  placeholder: {
    width: 81,
    height: 81,
    borderRadius: 40.5,
    backgroundColor: '#ccc', // Placeholder color
  },
});

export default Profile;