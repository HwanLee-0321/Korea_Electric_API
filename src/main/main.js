const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function createWindow () {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile(path.join(__dirname, '..', 'renderer', 'index.html'));
}

app.whenReady().then(() => {
  ipcMain.handle('fetch-kepco-data', () => {
    return new Promise((resolve, reject) => {
      const pythonProcess = spawn('python', ['main.py']);
      let dataString = '';

      pythonProcess.stdout.on('data', (data) => {
        dataString += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        reject(data.toString());
      });

      pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        resolve(dataString);
      });
    });
  });

  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});
