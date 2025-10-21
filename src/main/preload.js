const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  fetchKepcoData: () => ipcRenderer.invoke('fetch-kepco-data')
});
