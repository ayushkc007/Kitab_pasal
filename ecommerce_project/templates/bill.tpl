{% extends "mail_templated/base.tpl" %}

{% block subject %}
Order Placed!!
{% endblock %}

{% block body %}
{% endblock %}

{% block html %}
{{ user.username }}, <strong>Your order has been placed.</strong>
<body>
        
       <div class="invoice-box" style="max-width: 800px;margin: auto;padding: 30px;border: 1px solid #eee;box-shadow: 0 0 10px rgba(0, 0, 0, .15);font-size: 16px;line-height: 24px;font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;color: #555;">
          <img src="http://65.2.26.107/kitab-pasal.png" alt="Company logo" /><br>
          <p style="text-align:center;">
              <strong style="color: #555;">
                  Kitab Pasal<br />
                  Lokanthali, Thimi 1<br />
                  Bhaktapur, Nepal
              </strong>
          </p>
          <div style="position: relative;">

              <div style="right:0;position: absolute;text-align: end;color: #555;" >
                  Invoice #: {{invoice.id}}<br />
                  Created: {{invoice.payment_date}}<br />
              </div>

              <div style="text-align: start;position: absolute;left:0;color: #555;">
                  {{user.username}}<br />
                 Contact no: {{invoice.contact_no}}
              </div>
          </div>
            
          <table cellpadding="0" cellspacing="0" style="width: 100%;line-height: inherit;text-align: left;margin-top:15%;color: #555;">

            
            <tr class="heading">
                <td style="padding: 5px;vertical-align: top;background: #eee;border-bottom: 1px solid #ddd;font-weight: bold;color:white;background-color: #FE980F;">
                    Item
                </td>
                <td style="padding: 5px;vertical-align: top;text-align: right;background: #eee;border-bottom: 1px solid #ddd;font-weight: bold; color:white;background-color: #FE980F;">
                  Unit Price
              </td>
              <td style="padding: 5px;vertical-align: top;text-align: right;background: #eee;border-bottom: 1px solid #ddd;font-weight: bold; color:white;background-color: #FE980F;">
                Quantity
            </td>
                
                <td style="padding: 5px;vertical-align: top;text-align: right;background: #eee;border-bottom: 1px solid #ddd;font-weight: bold; color:white;background-color: #FE980F;">
                    Sub Amount
                </td>
            </tr>
            {% for invoice_detail in invoice_details %}
            <tr class="item">
                <td style="padding: 5px;vertical-align: top;border-bottom: 1px solid #eee;color: #555;">
                    {{invoice_detail.product}}
                </td>
                <td style="padding: 5px;vertical-align: top;text-align: right;border-bottom: 1px solid #eee;color: #555;">
                                {{invoice_detail.product.price}}
              </td>
              <td style="padding: 5px;vertical-align: top;text-align: right;border-bottom: 1px solid #eee;color: #555;">
                {{invoice_detail.quantity}}
            </td>
                
                <td style="padding: 5px;vertical-align: top;text-align: right;border-bottom: 1px solid #eee;color: #555;">
                    {{invoice_detail.sub_amount}}
                </td>
            </tr>
            {% endfor %}
            
            
            <tr class="total">
                <td style="padding: 5px;vertical-align: top;"></td>
                <td></td>
                <td></td>
                <td style="padding: 5px;vertical-align: top;text-align: right;border-top: 2px solid #FE980F;font-weight: bold;color: #555;">
                  
                   Tax @{{tax.tax_rate_in_percentage}}%: {{tax_amount}}
                </td>
            </tr>
            <tr class="total">
                <td style="padding: 5px;vertical-align: top;"></td>
                <td></td>
                <td></td>
                <td style="padding: 5px;vertical-align: top;text-align: right;border-top: 2px solid #FE980F;font-weight: bold;color: #555;">
                  
                   Shipping cost: Rs. {{shipping.shipping_cost}}
                </td>
            </tr>
            
            <tr class="total">
                <td style="padding: 5px;vertical-align: top;"></td>
                <td></td>
                <td></td>
                <td style="padding: 5px;vertical-align: top;text-align: right;border-top: 2px solid #FE980F;font-weight: bold;color: #555;">
                  
                   Total: Rs. {{invoice.total_amount}}
                </td>
            </tr>
        </table>
    </div>
    </body>
{% endblock %}