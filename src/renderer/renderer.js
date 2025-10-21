document.addEventListener('DOMContentLoaded', () => {
  const fetchDataBtn = document.getElementById('fetch-data');
  const dataContainer = document.getElementById('data-container');

  fetchDataBtn.addEventListener('click', async () => {
    dataContainer.textContent = 'Fetching data...';
    try {
      const data = await window.electronAPI.fetchKepcoData();
      const formattedData = JSON.stringify(JSON.parse(data), null, 2);
      dataContainer.textContent = formattedData;
    } catch (error) {
      dataContainer.textContent = `Error fetching data: ${error}`;
    }
  });
});
