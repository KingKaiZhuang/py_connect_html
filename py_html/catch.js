// 檔案在本地端的路徑
const filePath = 'path/to/your/folder/file.json';

// 使用 fetch 發送本地端檔案的請求
fetch(filePath)
  .then(response => {
    if (!response.ok) {
      throw new Error(`無法抓取檔案 ${filePath}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(`成功抓取檔案 ${filePath}：`, data);
  })
  .catch(error => {
    console.error('抓取檔案時發生錯誤：', error.message);
  });
