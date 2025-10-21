document.addEventListener('DOMContentLoaded', () => {
  const fetchDataBtn = document.getElementById('fetch-data');
  const dataContainer = document.getElementById('data-container');

  fetchDataBtn.addEventListener('click', async () => {
    dataContainer.textContent = '데이터를 가져오는 중...';
    try {
      const data = await window.electronAPI.fetchKepcoData();
      const formattedData = JSON.stringify(JSON.parse(data), null, 2);
      dataContainer.textContent = formattedData;
    } catch (error) {
      dataContainer.textContent = `데이터 가져오기 오류: ${error}`;
    }
  });
});
