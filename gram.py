# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:46:50 2021

@author: karen
"""
import numpy as np

def menu():
    
   j = 0
   a1 = np.array([[0.7140299],[0.6918437],[0.6748934],[0.7884872]])
   a2 = np.array([[0.6918437],[1.2492256],[1.0307285],[0.6275049]])
   a3 = np.array([[0.6748934],[1.0307285],[1.0893471],[0.5567456]])
   a4 = np.array([[0.7884872],[0.6275049],[0.5567456],[0.9550583]])
   
   

   while (j < 7):
       
       print("a1 = ",a1)
       print("a2 = ", a2)
       print("a3 = ",a3)
       print("a4 = ",a4)
    
       q1=a1/np.sqrt(a1[0][0]**2 +a1[1][0]**2+a1[2][0]**2+a1[3][0]**2)
       print("q1 = ",q1)
       
       q2_linha = a2 - np.matmul(q1,np.matmul(np.transpose(q1),a2))
       print("q2' = ",q2_linha)
       
       q2=q2_linha/np.sqrt(q2_linha[0][0]**2 +q2_linha[1][0]**2+q2_linha[2][0]**2+q2_linha[3][0]**2)
       print("q2 = ",q2)
       
       q3_linha = a3 -np.matmul(q1,np.matmul(np.transpose(q1),a3))-np.matmul(q2,np.matmul(np.transpose(q2),a3))
       print("q3' = ", q3_linha)
       
       q3=q3_linha/np.sqrt(q3_linha[0][0]**2 +q3_linha[1][0]**2+q3_linha[2][0]**2+q3_linha[3][0]**2)
       print("q3 = ", q3)
       
       q4_linha = a4 - np.matmul(q1,np.matmul(np.transpose(q1),a4)) -np.matmul(q2,np.matmul(np.transpose(q2),a4))-np.matmul(q3,np.matmul(np.transpose(q3),a4))
       print("q4' = ", q4_linha)
       
       q4 = q4_linha/np.sqrt(q4_linha[0][0]**2 +q4_linha[1][0]**2+q4_linha[2][0]**2+q4_linha[3][0]**2)
       print("q4 = ", q4)
       
       R=np.array([[np.dot(np.transpose(q1),a1)[0][0],np.dot(np.transpose(q1),a2)[0][0],np.dot(np.transpose(q1),a3)[0][0],np.dot(np.transpose(q1),a4)[0][0]],[0,np.dot(np.transpose(q2),a2)[0][0],np.dot(np.transpose(q2),a3)[0][0],np.dot(np.transpose(q2),a4)[0][0]],[0,0,np.dot(np.transpose(q3),a3)[0][0],np.dot(np.transpose(q3),a4)[0][0]],[0,0,0,np.dot(np.transpose(q4),a4)[0][0]]])
       print("R = ", R)    
    
      
       
       q1_modificado = []
       i = 0
       while i < 4:
           q1_modificado.append(q1[i][0])   
           i+= 1
           
       q2_modificado = []
       i = 0
       while i < 4:
           q2_modificado.append(q2[i][0])
           i+= 1
       
       q3_modificado = []
       i = 0
       while i < 4:
           q3_modificado.append(q3[i][0])
           i+= 1
           
       q4_modificado = []
       i = 0
       while i < 4:
           q4_modificado.append(q4[i][0])
           i+= 1
           
       Q = np.array([q1_modificado,q2_modificado,q3_modificado,q4_modificado])
       Q = np.transpose(Q)
       print("Q = ", Q)
      
       print("A = RQ = ", np.dot(R,Q))
       
       A = np.dot(R,Q)
     
       a1 = (A[:,0])
       k = 0
       a1_modificado = []
       while (k < 4):
           a1_modificado.append (a1[k])
           k += 1
        
       a1 = np.array([[a1_modificado[0]],[a1_modificado[1]],[a1_modificado[2]],[a1_modificado[3]]])
    
       a2 = (A[:,1])
       k = 0
       a2_modificado = []
       while (k < 4):
           a2_modificado.append (a2[k])
           k += 1
        
       a2 = np.array([[a2_modificado[0]],[a2_modificado[1]],[a2_modificado[2]],[a2_modificado[3]]])
       
       a3 = (A[:,2])
       k = 0
       a3_modificado = []
       while (k < 4):
           a3_modificado.append (a3[k])
           k += 1
        
       a3 = np.array([[a3_modificado[0]],[a3_modificado[1]],[a3_modificado[2]],[a3_modificado[3]]])
       
       a4 = (A[:,3]) 
       k = 0
       a4_modificado = []
       while (k < 4):
           a4_modificado.append (a4[k])
           k += 1
        
       a4 = np.array([[a4_modificado[0]],[a4_modificado[1]],[a4_modificado[2]],[a4_modificado[3]]])                                                                                                                                                                                       
   
       j += 1
     
    
    
menu()