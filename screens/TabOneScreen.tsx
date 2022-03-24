import * as React from 'react';
import { StyleSheet } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { RootTabScreenProps } from '../types';

export default function HomeScreen({ navigation }: RootTabScreenProps<'TabOne'>) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Incognito</Text>
      <Text style={styles.paragraph}>Please make use of this app!</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="/screens/TabOneScreen.tsx" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'white',
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    fontStyle: 'normal',
    fontFamily: 'Cochin',
    color: '#154c79',
  },
  paragraph: {
    margin: 24,
    fontSize: 16,
    fontWeight: 'normal',
    textAlign: 'center',
    color:'black',
  },
  separator: {
    marginVertical: 10,
    height: 1,
    width: '80%',
  },
});
