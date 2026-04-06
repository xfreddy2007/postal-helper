const form = document.getElementById('lookup-form');
const addressInput = document.getElementById('address');
const submitBtn = document.getElementById('submit-btn');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const address = addressInput.value.trim();
  if (!address) return;

  submitBtn.disabled = true;
  submitBtn.textContent = '查詢中…';
  resultDiv.className = 'result hidden';
  resultDiv.innerHTML = '';

  try {
    const resp = await fetch('/api/lookup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ address }),
    });

    const data = await resp.json();

    if (!resp.ok || data.error) {
      showError(data.error || '查詢失敗，請稍後再試。');
      return;
    }

    showSuccess(address, data);
  } catch {
    showError('無法連線至伺服器，請確認網路連線。');
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = '查詢';
  }
});

function showSuccess(address, data) {
  const zipcode = data.zipcode6 || data.zipcode;
  const is6digit = !!data.zipcode6;

  let html = `<div class="label">地址</div><div>${escapeHtml(address)}</div><br>`;

  if (zipcode) {
    const label = is6digit ? '郵遞區號（6碼）' : '郵遞區號（5碼，查無6碼）';
    html += `<div class="label">${label}</div><div class="zipcode">${escapeHtml(zipcode)}</div>`;
  } else {
    html += '<div>查無對應郵遞區號，請確認地址是否正確。</div>';
  }

  if (data.detail_url) {
    html += `<br><a href="${escapeHtml(data.detail_url)}" target="_blank" rel="noopener">查看詳細資訊 →</a>`;
  }

  resultDiv.innerHTML = html;
  resultDiv.className = 'result success';
}

function showError(message) {
  resultDiv.innerHTML = escapeHtml(message);
  resultDiv.className = 'result error';
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
