/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "adc_tags_gen_impl.h"

#include <iostream>

using namespace std;
using namespace gr::COWN_misc;





namespace gr {
  namespace COWN_misc {

    adc_tags_gen::sptr
    adc_tags_gen::make()
    {
      return gnuradio::get_initial_sptr
        (new adc_tags_gen_impl());
    }

    /*
     * The private constructor
     */
    adc_tags_gen_impl::adc_tags_gen_impl()
      : gr::block("adc_tags_gen",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
      counterp(0), d_state(SEARCH), timestamp(0), timestamp2(0), counter_shif(0), timestamp_meas(0), timestamp_meas2(0) 
    {}

    /*
     * Our virtual destructor.
     */
    adc_tags_gen_impl::~adc_tags_gen_impl()
    {
    }

    void
    adc_tags_gen_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        ninput_items_required[0] = noutput_items*2;
        set_output_multiple(66);   

    }

    int
    adc_tags_gen_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const float *in = (const float*) input_items[0];
        gr_complex *out = (gr_complex *) output_items[0];
        gr_complex   *in_c = (gr_complex*)in;
        gr_complex   *out_c = (gr_complex*)out;
        unsigned int *in_int  = (unsigned int*)in;
        unsigned int *out_int  = (unsigned int*)out;

        int noutput = noutput_items;
        int ninput  = ninput_items[0];

        //memcpy(out, in_c,   noutput_items* sizeof(gr_complex));
        counterp++;




          switch(d_state) {

         case SEARCH: { 


                int m = 0;
                int k = 0;

                int mur;
                mur = output_multiple();

                memcpy(out, in_c,   noutput_items* sizeof(gr_complex));
                while( k < ninput && k < noutput*2) {
                 

                  if (  (counterp %64 ==0)  and (k <128)  ){
                     


                    if(    in_int[k] == 0xffffffff  ) {

                      if(    in_int[k+3] == 0xffffffff  ) { 

                        if (timestamp - timestamp2 != 5120  ) {
                        cout << "***************************************" << endl;
                        cout << "HEADDER ERROR" << endl;
                        cout <<  hex << in_int[k]   <<  "\t" <<   dec<<  in_int[k]    <<"\t k = "<< k<< endl;
                        cout <<  hex << in_int[k+1] <<  "\t" <<   dec<<  in_int[k+1]  << endl;
                        cout <<  hex << in_int[k+2]   <<  "\t" <<   dec<<  in_int[k+2]    <<" k + 2 = "<< k+2<< endl;
                        cout <<  hex << in_int[k+3] <<  "\t" <<   dec<<  in_int[k+3]  << endl;
                        cout <<  "timestamp =\t"<<   timestamp << "\t elapsed time= \t"<<  timestamp/40e6 << endl;
                        cout << timestamp - timestamp2  << endl;


                        cout <<  "output_multiple =\t"<<  mur  << "\t noutput= " << noutput  <<   "\t ninput= " << ninput  << "\tcounter shit=\t"<< counter_shif <<  endl;

                        cout << "***************************************" << endl;
                        }
                      }
                    }


                  }


                  if(    in_int[k] == 0xffffffff  ) {
                    if(    in_int[k+3] == 0xffffffff  ) { 

                      timestamp2 = timestamp;
                      timestamp =  in_int[k+1]  +  (in_int[k+2]*(4294967296)) ;

                      timestamp_meas2 = timestamp_meas;
                      timestamp_meas = nitems_written(0) + k/2 - 16 +128;

                      unsigned int seq0 = in_int[k+1];
                      unsigned int seq1 = in_int[k+2] ;

                      float tiempok  =   k*1.00000;

                      uint64_t aesc =  timestamp_meas;


                      float time_diff_meas = (    (timestamp_meas - timestamp_meas2     )*1.0            );
                      float time_diff      = (    (timestamp - timestamp2     )*1.0            );


                      //memcpy( out+k, in_c-66,   66* sizeof(gr_complex));    //+(k/2)+2
                      m += 64;

                            const pmt::pmt_t key = pmt::string_to_symbol("time_diff");
                            const pmt::pmt_t value = pmt::from_float   (  time_diff);
                            const pmt::pmt_t srcid = pmt::string_to_symbol("sesentaycuatro");
                            add_item_tag(0,   aesc , key, value, srcid);
       
                            // std::string s = std::to_string(42) 
                            const pmt::pmt_t key2 =   pmt::string_to_symbol("time_diff_meas");
                            const pmt::pmt_t value2 = pmt::from_float   (  time_diff_meas );
                            const pmt::pmt_t srcid2 = pmt::string_to_symbol("sesentaycuatro");
                            add_item_tag(0,   aesc , key2, value2, srcid2);

                            const pmt::pmt_t key3 =   pmt::string_to_symbol("k_value/2");
                            const pmt::pmt_t value3 = pmt::from_float   (  tiempok/2 );
                            const pmt::pmt_t srcid3 = pmt::string_to_symbol("sesentaycuatro");
                            add_item_tag(0,   aesc , key3, value3, srcid3);
                            
                            const pmt::pmt_t key4 =   pmt::string_to_symbol("noutputs");
                            const pmt::pmt_t value4 = pmt::from_float   (  noutput*1.0 );
                            const pmt::pmt_t srcid4 = pmt::string_to_symbol("sesentaycuatro");
                            add_item_tag(0,   aesc , key4, value4, srcid4);


                                char buffer[50];

                                int n;
                                n=sprintf(buffer, "0x%x ", seq0 );

                                const pmt::pmt_t key6 =   pmt::string_to_symbol("seq0");
                                const pmt::pmt_t value6 = pmt::string_to_symbol( buffer );
                                const pmt::pmt_t srcid6 = pmt::string_to_symbol("sesentaycuatro");
                                add_item_tag(0,   aesc , key6, value6, srcid6);  






                            if (time_diff != 5120  && time_diff > 12000){
                                counter_shif++;
                                const pmt::pmt_t key5 =   pmt::string_to_symbol("BAD TAG");
                                const pmt::pmt_t value5 = pmt::from_float   (  time_diff/80.0 );
                                const pmt::pmt_t srcid5 = pmt::string_to_symbol("sesentaycuatro");
                                add_item_tag(0,   aesc , key5, value5, srcid5);









                            }



                    }


                  } 


                    k++;
                }

                consume(0, noutput_items*2);


                return noutput_items;

          }

         case COPY: { 
            cout << " copu" << endl;
           
           consume_each (noutput_items*2);
           return 0;
         }


      }


    }

  void insert_tag(uint64_t item) {
    // mylog(boost::format("frame start at %1%") % item);

    const pmt::pmt_t key = pmt::string_to_symbol("section_start");
    const pmt::pmt_t value = pmt::PMT_T;
    const pmt::pmt_t srcid = pmt::PMT_F;   //pmt::string_to_symbol("sesentaycuatro");
    //gr::block::add_item_tag(0, item, key, value, srcid);
  }





  } /* namespace  COWN_misc */
} /* namespace gr */







































 


 

 
    
 
 
